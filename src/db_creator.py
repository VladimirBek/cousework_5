class DBMaker:

    @staticmethod
    def create_database(db_name, cur):
        cur.execute(f'DROP DATABASE IF EXISTS {db_name}')
        cur.execute(f'CREATE DATABASE {db_name}')

    @staticmethod
    def create_table_vacancies(cur):
        cur.execute('DROP TABLE IF EXISTS vacancies')
        cur.execute('''CREATE TABLE vacancies(vacancy_id serial PRIMARY KEY,
                    vacancy_name varchar(100),
                    employer_name varchar(50),
                    salary_from integer,
                    salary_to integer,
                    address text,
                    city varchar(50),
                    employer_id smallint)''')

    @staticmethod
    def create_table_employers(cur):
        cur.execute('DROP TABLE IF EXISTS employers')
        cur.execute('CREATE TABLE employers(employer_id serial PRIMARY KEY,'
                    'employer_name varchar(100),'
                    'address text,'
                    'city varchar(50),'
                    'vacancies_count smallint)')

    @staticmethod
    def fill_vacancies_table(cur, vacancy_name, employer_name, salary_from, salary_to, address, city, employer_id):
        cur.execute(
            f'''INSERT INTO vacancies (vacancy_name, salary_from, salary_to, address, city, employer_id)
                VALUES ( 
                {vacancy_name},
                {employer_name} 
                {salary_from}, 
                {salary_to},
                {address},
                {city},
                {employer_id});'''
        )

    @staticmethod
    def fill_employers_table(cur, employer_name, address, city, vacancies_count):
        cur.execute(
            f'''INSERT INTO vacancies (employer_name, address, city, vacancies_count)
                        VALUES ( 
                        {employer_name}, 
                        {address}, 
                        {city},
                        {vacancies_count};'''
        )
