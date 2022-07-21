import sqlite3 as lite


# functionality goes here

class DatabaseManage(object):

    def __init__(self):
        global con
        try:
            con = lite.connect('courses.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("Unable to made connection with database!")
        

    #TODO: create data
    def insertData(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO course(name, description, price, is_private) VALUES (?,?,?,?)", data
                )
                return True
        except Exception:
            return False

    #TODO: read data
    def fetchData(self):
        try:
            with con:
                cur = con.cursor()
                sql = "SELECT *  FROM course"
                cur.execute(sql)
                return cur.fetchall()
        except Exception:
            return False

    #TODO: delete data
    def deleteData(self, id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM course WHERE id = ?"
                cur.execute(sql, [id])
                return True
        except Exception:
            return False

# TODO: provide interface to user   
def main():
    print("*"*20)
    print("\n:: course management :: \n")
    print("*"*40)
    print("\n")
    
    db = DatabaseManage()
    print("*"*40)
    print("\n :: User Manual :: \n")
    print("*"*40)

    print('\nPress 1. Insert a new course')
    print('\nPress 2. Show all courses')
    print('\nPress 3. Delete a course (NEED ID OF COURSE)')
    print("*"*40)
    print("\n")
    
    choice = input("\n Enter a choise: ")
    
    if choice == "1":
        name = input("\n Enter course name: ")
        description = input("\n Enter course description: ")
        price = input("\n Enter course price: ")
        private = input("\n Is this course private(0/1): ")

        if db.insertData([name, description, price, private]):
            print("Course is inserted successfully")
        else:
            print("Oops! Something is wrong")

    elif choice == "2":
        print("\n :: course list ::")
        for index, item in enumerate(db.fetchData()):
            print("\n SL no : " + str(index + 1)) 
            print("Course ID : " + str(item[0])) 
            print("Course name : " + str(item[1])) 
            print("Course des : " + str(item[2])) 
            print("Course price : " + str(item[3])) 
            private = "Yes" if item[4] else 'No'
            print("Course private : " + private) 
            print("\n") 

    elif choice == "3":
        courseId = input("Enter a course ID: ")
        
        if db.deleteData(courseId):
            print("course id deleted successfully")
        else:
            print('Oops something wrong')
    
    else:
        print("Invalid choise")
        
if __name__ == '__main__':
    main()
            