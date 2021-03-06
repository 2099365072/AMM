#!/usr/bin/env python3
"""
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* Audiophiles Music Manager          Build 20180119          VER0.0.0PREALPHA *
* (C)2017 Mattijs Snepvangers                           pegasus.ict@gmail.com *
* lib/db_agent.py                    Database Agent          VER0.0.0PREALPHA *
* License: MIT                             Please keep my name in the credits *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""

class DBagent :
    """Database agent

    will manage and interface with SQLite or MySQL DB"""
    def __init__(self):
        # my_sql = None
        # my_sql_errorcode = None
        self.db_connect_info = ammConfig.get(db_connect_info)
        import mysql.connector as my_sql
        from mysql.connector import errorcode as my_sql_errorcode

    @classmethod
    def connect(self):
        """connect to DB

        """
        db_port = self.db_connect_info("db_port")
        db_host = self.db_connect_info("host")

        if db_port != 3306:
            db_host = db_host + ":" + db_port
        #connect to database, display error if something goes wrong
        try:
            __my_db = my_sql.connect(DBuser, DBpass, db_host, DB)
        except my_sql.Error as my_sql_error:
            if my_sql_error == my_sql_errorcode.ER_ACCESS_DENIED_ERROR:
                print("Authentication error")
            elif my_sql_error == my_sql_errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(my_sql_error)

    @classmethod
    def db_create(self, sql_struct):
        """ create DB, tables and structure """
        pass

    @classmethod
    def update_record(self): # , table, record
        """method to update a record in a given table

        """
        pass

    @classmethod
    def run_query(self, query):
        """method to run query"""
        query_result = my_sql(query)
        return query_result

def main():
    """just in case somebody wants to test this file by itself"""
    print("It works!!!")
    ###TODO### do something with the various methods/functions of this file

# standard boilerplate
if __name__ == '__main__':
    main()
