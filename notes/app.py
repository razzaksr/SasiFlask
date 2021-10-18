from datetime import datetime
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# db configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/test'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
base=SQLAlchemy(app)


#model
class notes(base.Model):
    id=base.Column(base.Integer,primary_key=True)
    title=base.Column(base.String(255),nullable=False)
    what=base.Column(base.String(255),nullable=False)
    doc=base.Column(base.DateTime,default=datetime.utcnow)

    def __init__(self,title,what):
        self.title=title
        self.what=what

    def __repr__(self) -> str:
        return f"{self.title} - {self.what}"


@app.route('/',methods=['GET','POST'])
def first():
    if request.method=="POST":
        pro=notes(request.form["title"],request.form["what"])
        base.session.add(pro)
        base.session.commit()
        return render_template('home.html')
    else:
        #base.create_all()
        '''pro=notes('simple','sample')
        base.session.add(pro)
        base.session.commit()'''
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True,port=8000)