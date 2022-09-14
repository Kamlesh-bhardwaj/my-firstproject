from flask import Flask,render_template ,url_for,redirect,request,flash
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

app.secret_key= "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:''@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)


class Data(db.Model):
    id=db.Column(db.Integer,  primary_key  = True)
    ProjectName =db.Column(db.String(1000))
    Objective =db.Column(db.String(1000))
    Agency =db.Column(db.String(1000))
    ProjectsLeadfromJSHLsside =db.Column(db.String(1000))
    Otherdepartmentsunitsinvolvedintheproject =db.Column(db.String(1000))
    StartDate =db.Column(db.String(1000))
    EndDate =db.Column(db.String(1000))
    ProjectCost =db.Column(db.String(1000))
    ProjectorrealizedsavingsbenefitsROI =db.Column(db.String(1000))
    ContractDocumentspleaseattach =db.Column(db.String(1000))
    CurrentStatuspleaseprovidesummaryofcurrentstatus=db.Column(db.String(1000))



def ___init__(self, ProjectName,Objective,Agency,ProjectsLeadfromJSHLsside,Otherdepartmentsunitsinvolvedintheproject,StartDate,EndDate,ProjectCost,ProjectorrealizedsavingsbenefitsROI,ContractDocumentspleaseattach,CurrentStatuspleaseprovidesummaryofcurrentstatus):
    self.ProjectName=ProjectName
    self.Objective=Objective
    self.Agency= Agency
    self.ProjectsLeadfromJSHLsside=ProjectsLeadfromJSHLsside
    self.Otherdepartmentsunitsinvolvedintheproject=Otherdepartmentsunitsinvolvedintheproject
    self.StartDate=StartDate
    self.EndDate=EndDate
    self.ProjectCost=ProjectCost
    self.ProjectorrealizedsavingsbenefitsROI=ProjectorrealizedsavingsbenefitsROI
    self.ContractDocumentspleaseattach=ContractDocumentspleaseattach
    self.CurrentStatuspleaseprovidesummaryofcurrentstatus=CurrentStatuspleaseprovidesummaryofcurrentstatus



    




@app.route('/')
def Index():
    all_data =Data.query.all()

    return render_template("index.html",projects=all_data)


@app.route('/insert', methods = ['POST'])
def insert():


    if request.method == 'POST':


        ProjectName = request.form['ProjectName']
        Objective = request.form['Objective']
        Agency = request.form['Agency']
        ProjectsLeadfromJSHLsside = request.form['ProjectsLeadfromJSHLsside']
        Otherdepartmentsunitsinvolvedintheproject = request.form['Otherdepartmentsunitsinvolvedintheproject']
        StartDate = request.form['StartDate']
        EndDate = request.form['EndDate']
        ProjectCost = request.form['ProjectCost']
        ProjectorrealizedsavingsbenefitsROI = request.form['ProjectorrealizedsavingsbenefitsROI']
        ContractDocumentspleaseattach = request.form['ContractDocumentspleaseattach']
        CurrentStatuspleaseprovidesummaryofcurrentstatus = request.form['CurrentStatuspleaseprovidesummaryofcurrentstatus']    


        my_data = Data (ProjectName=ProjectName,Objective=Objective,Agency=Agency,ProjectsLeadfromJSHLsside=ProjectsLeadfromJSHLsside,Otherdepartmentsunitsinvolvedintheproject=Otherdepartmentsunitsinvolvedintheproject,StartDate=StartDate,EndDate=EndDate,ProjectCost=ProjectCost,ProjectorrealizedsavingsbenefitsROI=ProjectorrealizedsavingsbenefitsROI,ContractDocumentspleaseattach=ContractDocumentspleaseattach,CurrentStatuspleaseprovidesummaryofcurrentstatus=CurrentStatuspleaseprovidesummaryofcurrentstatus)
        print(my_data)
        db.session.add(my_data)

        db.session.commit()

        flash("Project Inserted Succuessfully")

        return redirect (url_for('Index'))



@app.route('/update',methods= ['GET','POST'])
def update():
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get("id"))


        my_data.ProjectName = request.form['ProjectName']
        my_data.Objective = request.form['Objective']
        my_data.Agency = request.form['Agency']
        my_data.ProjectsLeadfromJSHLsside = request.form['ProjectsLeadfromJSHLsside']
        my_data.Otherdepartmentsunitsinvolvedintheproject = request.form['Otherdepartmentsunitsinvolvedintheproject']
        my_data.StartDate = request.form['StartDate']
        my_data.EndDate = request.form['EndDate']
        my_data.ProjectCost = request.form['ProjectCost']
        my_data.ProjectorrealizedsavingsbenefitsROI = request.form['ProjectorrealizedsavingsbenefitsROI']
        my_data.ContractDocumentspleaseattach = request.form['ContractDocumentspleaseattach']
        my_data.CurrentStatuspleaseprovidesummaryofcurrentstatus = request.form['CurrentStatuspleaseprovidesummaryofcurrentstatus']  


        db.session.commit()
        flash("Projects Update Successfully")

        return redirect(url_for('Index'))


@app.route('/delete/<id>/',methods =['GET','POST'])
def delete(id):
    my_data =Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Project Delete Successfully")

    return redirect(url_for('Index'))
         

    



        



if __name__=="__main__":
    app.run(debug=True)

    