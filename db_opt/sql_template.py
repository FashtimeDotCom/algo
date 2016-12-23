# coding:utf-8


class SqlTemplate(object):
    def __init__(self):
        # 任务定制模板
        self.update = """UPDATE {table} SET {sets} WHERE id={id_}"""
        self.insert = """INSERT INTO {table} {key} VALUES {value}"""
        self.select = """SELECT * FROM {table} WHERE job_id={job_id} AND step={step}"""

    def sql_update(self, data):
        sets_ = []
        tmp = "{key}={value!r}"
        for key,value in data.get('sets').iteritems():
            sets_.append(tmp.format(key=key, value=value))

        return self.update.format(table=data.get("table"),
            sets=", ".join(sets_),
            id_=data.get("id_"),
            )

    def sql_insert(self, data):
        keys = []
        values = []
        tmp = "%({key})s"
        for key in data.get('data').keys():
            keys.append(key)
            values.append(tmp.format(key=key))
        
        return self.insert.format(table=data.get("table"),
            key="("+", ".join(keys)+")",
            value="("+", ".join(values)+")",
            )

    def sql_select(self, data):
        return self.select.format(table=data.get("table"),
            job_id=data.get("job_id"),
            step=data.get("step"),
            )
