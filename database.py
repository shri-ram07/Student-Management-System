from tkinter import messagebox
import mysql.connector as sql


from Function_def import convert_to_binary


class Database:
    def __init__(self):
        self.cnx = sql.connect(host='localhost', user='root', password='anam', database='teacher_auth')
        self.cursor = self.cnx.cursor()
        self.li = []
    def delete_std(self,roll):
        if self.check(roll):
            query = "DELETE FROM student_records WHERE Roll_Number = %s"
            data = (f'{roll}',)

            # Execute the query
            self.cursor.execute(query, data)

            # Commit the transaction
            self.cnx.commit()

            # Close the cursor and connection
            self.msgdel = messagebox.showinfo("Deletion Successfully",
                                           "YOUR DATA HAS BEEN DELETED SUCCESSFULLY👍")
        else:
            self.error2 = messagebox.showinfo("Deletion UnSuccessfully",
                                                 "Data Not Foundt !")

    def fetch_teach(self,id,password):
        data = []
        self.cursor.execute("use teacher_auth")
        self.cnx.commit()
        self.cursor.execute("select * from uid_pass")
        for row in self.cursor:
            row = list(row)
            if str(row[0]) == id and row[1] == password:
                for dt in row:
                    data.append(dt)
        return(data)

    def auth(self,id,password):
        authentication = None
        self.cursor.execute("use teacher_auth")
        self.cnx.commit()
        self.cursor.execute("select * from uid_pass")
        for row in self.cursor:
            row=list(row)
            if str(row[0])==id and row[1]==password:
                authentication=True
                break
            else:
                authentication=False
        return authentication
    def entry_std(self,values,roll):
        if self.check(roll):
            self.error = messagebox.showinfo("Insertion UnSuccessfully",
                                           "Data Already Exist !")

        else:
            # Your SQL insert query
            query = """
            INSERT INTO student_records (
                Roll_Number, Name, Fathers_Name, Mothers_Name, Gender, Mobile, Email, 
                Class_Group, Institute_Name, std_pic_for_sql, E_E1, E_E5, E_E3, E_E7, 
                Ma_E1, Ma_E5, Ma_E3, Ma_E7, H_E1, H_E5, H_E3, H_E7, Sc_E1, Sc_E5, 
                Sc_E3, Sc_E7, Ss_E1, Ss_E5, Ss_E3, Ss_E7, Max_Marks, Total_obtained_marks, 
                Percentage
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s
            );
            """


            # Data to be inserted


            # Execute the query
            self.cursor.execute(query, values)

            # Commit the transaction
            self.cnx.commit()

            # Close the cursor and connection

            self.msg = messagebox.showinfo("Insertion Successfully",
                                           "YOUR DATA HAS BEEN SAVED SUCCESSFULLY👍")

    def entry_tech(self):
        user_id = int(input("Enter UserId (Numerical only !) : "))
        password = input("Enter PassWord: ")
        name = input("Enter Name : ")
        mobile = input("Enter Mobile Number : ")
        email = input("Enter Email : ")
        post = input("Enter post : ")
        photo = convert_to_binary(input("Enter Image Address : "))

        # Your SQL insert query
        query = """
        INSERT INTO uid_pass (id, pass, name, mobile, email, post, photo)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        # Data to be inserted
        data = (user_id, password, name, mobile, email, post,
                photo)

        # Execute the query
        self.cursor.execute(query, data)

        # Commit the transaction
        self.cnx.commit()

        # Close the cursor and connection
        self.cursor.close()
        self.cnx.close()
        print("## Data Entered successfully ##")

    def check(self, roll):
        li = []
        query = "SELECT * FROM student_records WHERE Roll_Number = %s"
        self.cursor.execute(query, (roll,))  # Pass 'roll' as a tuple
        for row in self.cursor:
            li.append(row)
        return len(li) > 0

    def fetch_std(self, roll):
        li = []
        query = "SELECT * FROM student_records WHERE Roll_Number = %s"
        self.cursor.execute(query, (roll,))  # Pass 'roll' as a tuple
        for row in self.cursor:
            for el in row:
                li.append(el)
        return li

if __name__=="__main__":
    mo = Database()
    print(mo.fetch_std(1)[9])