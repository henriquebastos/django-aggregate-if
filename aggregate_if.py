# coding: utf-8
'''
Implements conditional aggregates.

This code was based on the work of others found on the internet:

1. http://web.archive.org/web/20101115170804/http://www.voteruniverse.com/Members/jlantz/blog/conditional-aggregates-in-django
2. https://code.djangoproject.com/ticket/11305
3. https://groups.google.com/forum/?fromgroups=#!topic/django-users/cjzloTUwmS0
4. https://groups.google.com/forum/?fromgroups=#!topic/django-users/vVprMpsAnPo
'''
from django.db.models.aggregates import Aggregate as DjangoAggregate
from django.db.models.sql.aggregates import Aggregate as DjangoSqlAggregate


class SqlAggregate(DjangoSqlAggregate):
    conditional_template = '%(function)s(CASE WHEN %(condition)s THEN %(field)s ELSE null END)'

    def __init__(self, col, source=None, is_summary=False, condition=None, **extra):
        super(SqlAggregate, self).__init__(col, source, is_summary, **extra)
        self.condition = condition

    def relabel_aliases(self, change_map):
        super(SqlAggregate, self).relabel_aliases(change_map)
        if self.has_condition:
            self.condition.relabel_aliases(change_map)

    def as_sql(self, qn, connection):
        if self.has_condition:
            self.sql_template = self.conditional_template
            self.extra['condition'] = self._condition_as_sql(qn, connection)

        return super(SqlAggregate, self).as_sql(qn, connection)

    @property
    def has_condition(self):
        # Warning: bool(QuerySet) will hit the database
        return self.condition is not None

    def _condition_as_sql(self, qn, connection):
        '''
        Return sql for condition.
        '''
        escape = lambda p: qn(p) if isinstance(p, basestring) else p
        sql, param = self.condition.query.where.as_sql(qn, connection)
        param = map(escape, param)

        return sql % tuple(param)


class SqlSum(SqlAggregate):
    sql_function = 'SUM'


class Aggregate(DjangoAggregate):
    def __init__(self, lookup, only=None, **extra):
        super(Aggregate, self).__init__(lookup, **extra)
        self.only = only
        self.condition = None

    def add_to_query(self, query, alias, col, source, is_summary):
        if self.only:
            self.condition = query.model._default_manager.filter(self.only)

        aggregate = self.sql_klass(col, source, is_summary, self.condition, **self.extra)
        query.aggregates[alias] = aggregate


class Sum(Aggregate):
    name = 'Sum'
    sql_klass = SqlSum
