from flask import Flask, render_template, request
import gspread
gc=gspread.service_account(filename="Profile.json")
sh= gc.open("Perfil_cv")
shProfile=sh.get_worksheet(0)
shContacts=sh.get_worksheet(1)
app= Flask(__name__,template_folder='templates')

@app.route("/",methods=["POST","GET"])
def home():
 if request.method=="POST":
  shContacts.append_row([request.form["name"],request.form["Email"],request.form["mensaje"]])
 profile ={
  "About":shProfile.acell("B1").value,
  "Interests":shProfile.acell("B2").value,
  "Experience":shProfile.acell("B3").value,
  "Education":shProfile.acell("B4").value,
 }
 return render_template("home.html",profile=profile)
@app.route("/contact")
def contact():
 return render_template("contact.html")

if __name__ =="__main__":
 app.run(debug=True)