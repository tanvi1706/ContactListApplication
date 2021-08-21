import re
from django.shortcuts import render, HttpResponse
import MySQLdb
# Create your views here.

tables = ['contact', 'address', 'phone', 'date']

def home(request):
    return render(request, 'contacts/base.html')

def insert(request):
    return render(request, 'contacts/insert.html')

def add_data(request):
    if request.method == 'POST':
        print(request.POST)
        try:
            fname = request.POST.get("fname") if request.POST.get("fname") else ''
            mname = request.POST.get("mname") if request.POST.get("mname") else ''
            lname = request.POST.get("lname") if request.POST.get("lname") else ''
            address_type = request.POST.get("address_type") if request.POST.get("address_type") else ''
            address = request.POST.get("address") if request.POST.get("address") else ''
            city = request.POST.get("city") if request.POST.get("city") else ''
            state = request.POST.get("state") if request.POST.get("state") else ''
            zip = request.POST.get("zip") if request.POST.get("zip") else None
            phone_type = request.POST.get("phone_type") if request.POST.get("phone_type") else ''
            area_code = request.POST.get("area_code") if request.POST.get("area_code") else None
            number = request.POST.get("number") if request.POST.get("number") else None
            date_type = request.POST.get("date_type") if request.POST.get("date_type") else ''
            d_date = request.POST.get("d_date") if request.POST.get("d_date") else ''
            db = MySQLdb.connect(user='root', db='contactList', passwd='wqs95oUm', host='localhost')
            cursor = db.cursor()
            cursor.execute("INSERT INTO contact (fname, mname, lname) VALUES (%s, %s, %s)", (fname, mname, lname))
            cursor.execute("SELECT contact_id FROM contact WHERE fname = %s AND mname = %s AND lname = %s", (fname, mname, lname))
            contact_id = cursor.fetchall()[0][0]
            cursor.execute("INSERT INTO  address (contact_id, address_type, address, city, state, zip) VALUES (%s, %s, %s, %s, %s, %s)", (contact_id, address_type, address, city, state, zip))
            cursor.execute("INSERT INTO phone (contact_id, phone_type, area_code, number) VALUES (%s, %s, %s, %s)", (contact_id, phone_type, area_code, number))
            cursor.execute("INSERT INTO date (contact_id, date_type, d_date) VALUES (%s, %s, %s)", (contact_id, date_type, d_date))
            db.commit()
        except:
            db.rollback()
            return HttpResponse("<h1>error occured</h1>")
        db.close()
    return HttpResponse("<h1>Added Successfully.</h1>")

def find(request):
    return render(request, 'contacts/search.html')

def Search(request):
    if request.method == 'POST':
        dictionary = request.POST
        fetch_from_table = None
        for tablename in tables:
            if tablename in dictionary:
                fetch_from_table = tablename
        fieldname = dictionary[fetch_from_table]
        fieldvalue = request.POST.get("fieldvalue")
        query = "SELECT * FROM " + fetch_from_table + " WHERE " + fieldname + " = %s "
        db = MySQLdb.connect(user='root', db='contactList', passwd='wqs95oUm', host='localhost')
        cursor = db.cursor()
        #cursor.execute("SELECT * FROM " + fetch_from_table + " WHERE " + fieldname + "= %s", (fieldvalue,))
        cursor.execute(query, (fieldvalue,))
        datafetched = [row for row in cursor.fetchall()]
        items = []
        for d in datafetched:
            item = {}
            if fetch_from_table == 'contact':
                c_id = d[0]
                item['contact_id'] = c_id
            else:
                c_id = d[1]
                item['contact_id'] = c_id
            cursor.execute("SELECT * FROM contact WHERE contact_id = %s", (c_id,))
            data = [row for row in cursor.fetchall()]
            for x in data:
                item['fname'] = x[1]
                item['mname'] = x[2]
                item['lname'] = x[3]
            cursor.execute("SELECT * FROM address WHERE contact_id = %s", (c_id,))
            data = [row for row in cursor.fetchall()]
            for i in data:
                s = i[2]
                item[s+"_address"] = i[3]
                item[s+"_city"] = i[4]
                item[s+"_state"] = i[5]
                item[s+"_zip"] = i[6]
            cursor.execute("SELECT * FROM phone WHERE contact_id = %s", (c_id,))
            data = [row for row in cursor.fetchall()]
            for i in data:
                s = i[2]
                item[s+"_phone"] = i[4]
                item[s+"_area_code"] = i[3]
            cursor.execute("SELECT * FROM date WHERE contact_id = %s", (c_id,))
            data = [row for row in cursor.fetchall()]
            for i in data:
                s = i[2]
                item[s+"_date"] = i[3]
            items.append(item)
        db.close()
    return render(request,'contacts/cont.html',{"obj": items})


def deleteContact(request):
    return render(request, 'contacts/deleteForm.html')

def delete_data(request):
    if request.method == 'POST':
        try:
            c_id = request.POST.get("contact_id")
            db = MySQLdb.connect(user='root', db='contactList', passwd='wqs95oUm', host='localhost')
            cursor = db.cursor()
            cursor.execute("DELETE FROM contact WHERE contact_id = %s",(c_id,))
            db.commit()
        except:
            db.rollback()
            return HttpResponse("<h1>error occured</h1>")
        db.close()
    return HttpResponse("<h1>delete Successfully.</h1>")


def modifyContact(request):
    return render(request, 'contacts/modifyContact.html')

def modify_data(request):
    if request.method == 'POST':
        try:
            dictionary = request.POST
            print(dictionary)
            c_id = dictionary["contact_id"]
            fetch_from_table = None
            for tablename in tables:
                if tablename in dictionary:
                    fetch_from_table = tablename
            fieldname = dictionary[fetch_from_table]
            fieldvalue = request.POST.get("fieldvalue")
            db = MySQLdb.connect(user='root', db='contactList', passwd='wqs95oUm', host='localhost')
            cursor = db.cursor()
            if fetch_from_table == 'contacts':
                query = "UPDATE " + fetch_from_table + " SET " + fieldname + " = %s " + "WHERE contact_id = %s"
                cursor.execute(query, (fieldvalue, c_id))
            elif fetch_from_table == 'address':
                address_type = dictionary['address_type']
                query = "UPDATE " + fetch_from_table + " SET " + fieldname + " = %s " + "WHERE contact_id = %s" + "AND address_type = %s"
                cursor.execute(query, (fieldvalue, c_id, address_type))
            elif fetch_from_table == 'phone':
                phone_type = dictionary['phone_type']
                query = "UPDATE " + fetch_from_table + " SET " + fieldname + " = %s " + "WHERE contact_id = %s" + "AND phone_type = %s"
                cursor.execute(query, (fieldvalue, c_id, phone_type))
                print("fieldname", fieldname)
                if fieldname == 'number':
                    code = fieldvalue[0:3]
                    print("code",code)
                    query = "UPDATE " + fetch_from_table + " SET area_code "+ " = %s" + " WHERE contact_id = %s" + "AND phone_type = %s"
                    cursor.execute(query, (code, c_id, phone_type))
            elif fetch_from_table == 'date':
                date_type = dictionary['date_type']
                query = "UPDATE " + fetch_from_table + " SET " + fieldname + " = %s " + "WHERE contact_id = %s" + "AND date_type = %s"
                cursor.execute(query, (fieldvalue, c_id, date_type))
            db.commit()  
        except:
            db.rollback()
            return HttpResponse("<h1>error occured</h1>")
        db.close()
    return HttpResponse("<h1>updated Successfully</h1>")            