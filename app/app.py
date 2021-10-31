   
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href2='')
    else:
        value_slim = 29
        value_skinny = 30
        value_regular = 32
        value_relaxed = 34
        value_loose = 35
        num_slim = request.form['slim']
        num_skinny = request.form['skinny']
        num_regular = request.form['regular']
        num_relaxed = request.form['relaxed']
        num_loose = request.form['loose']
        total_slim = int(num_slim)*value_slim
        total_skinny = int(num_skinny)*value_skinny
        total_regular = int(num_regular)*value_regular
        total_relaxed = int(num_relaxed)*value_relaxed
        total_loose = int(num_loose)*value_loose
        final_result = total_slim + total_skinny + total_regular + total_relaxed + total_loose 
        return render_template('index.html', href2='slim='+num_slim+', skinny='+num_skinny+', regular='+num_regular+', relaxed='+num_relaxed+', loose='num_loose+', Total = '+str(final_result))
