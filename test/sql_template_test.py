# coding:utf-8

from db_opt import sql_template



st = sql_template.SqlTemplate()

print st.sql_update({"table": "job_info",
    "sets":{"status": 1, "job_type": "atubo"},
    "id_": 50,
    })
print "#"*100
print st.sql_insert({"table":"job_info",
    "data": {"status": 2, "job_type": "atubo"},
    })
print "#"*100
print st.sql_select({"table": "job_info",
    "job_id":5,
    "step": 1,
    })
