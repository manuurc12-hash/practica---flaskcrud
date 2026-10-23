from flask import Blueprint, flash, redirect, render_template, request, url_for

from db import database_cursor

contacts = Blueprint("contacts", __name__, template_folder="templates")


@contacts.route("/")
def Index():
    with database_cursor() as (_, cursor):
        cursor.execute("SELECT * FROM contacts")
        data = cursor.fetchall()
    return render_template("index.html", contacts=data)


@contacts.route("/add_contact", methods=["POST"])
def add_contact():
    fullname = request.form["fullname"]
    phone = request.form["phone"]
    email = request.form["email"]
    with database_cursor() as (connection, cursor):
        cursor.execute(
            "INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)",
            (fullname, phone, email),
        )
        connection.commit()
    flash("Contact Added successfully")
    return redirect(url_for("contacts.Index"))


@contacts.route("/edit/<int:contact_id>")
def get_contact(contact_id):
    with database_cursor() as (_, cursor):
        cursor.execute("SELECT * FROM contacts WHERE id = %s", (contact_id,))
        contact = cursor.fetchone()
    if contact is None:
        return "Contact not found", 404
    return render_template("edit-contact.html", contact=contact)


@contacts.route("/update/<int:contact_id>", methods=["POST"])
def update_contact(contact_id):
    fullname = request.form["fullname"]
    phone = request.form["phone"]
    email = request.form["email"]
    with database_cursor() as (connection, cursor):
        cursor.execute(
            """
            UPDATE contacts
            SET fullname = %s,
                email = %s,
                phone = %s
            WHERE id = %s
            """,
            (fullname, email, phone, contact_id),
        )
        connection.commit()
    flash("Contact Updated Successfully")
    return redirect(url_for("contacts.Index"))


@contacts.route("/delete/<int:contact_id>", methods=["POST", "GET"])
def delete_contact(contact_id):
    with database_cursor() as (connection, cursor):
        cursor.execute("DELETE FROM contacts WHERE id = %s", (contact_id,))
        connection.commit()
    flash("Contact Removed Successfully")
    return redirect(url_for("contacts.Index"))
