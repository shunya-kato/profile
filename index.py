from flask import Flask, render_template, redirect,url_for,request,session

app=Flask(__name__)
app.secret_key = 'jagioeheiII3SJ695i3i5ofi'

@app.route('/<name>')
def main(name):
    templname=name+'.htm'
    loginuser=session.get('loginuser',None)
    return render_template(templname,path=name,loginuser=loginuser)

@app.route('/')
def root():
    #return redirect(url_for('main',name='index'))
    loginuser = session.get('loginuser',None)
    if loginuser:
        return f'''welcome {loginuser}.<br>return <a href = "{ url_for('main',name='index')}">home</a>.'''
    else:
        #url_forの中身は呼び出したい関数
        login_url = url_for('login_get')
        return f'''\
            You have not logged in.<br>
            Please <a href = "{login_url}">login</a> first'''

@app.route('/login',methods=['GET'])
def login_get():
    loginuser = session.get('loginuser',None)
    if loginuser:
        #already logged in
        return f'already logged in as {loginuser}.'
    else:
        #show login form
        return '''\
            <form method="post" action="">
            Account: <input type="text" name="account"/><br>
            Password: <input type="password" name="password"/><br>
            <input type="submit" value="Login"/>
            </form>'''

@app.route('/login',methods=['POST'])
def login_post():
    account = request.form['account']
    password = request.form['password']

    loginpassword = 'helloworld'
    login_url = url_for('login_get')

    if password == loginpassword:
        session['loginuser'] = account
        return redirect(url_for('root'))
    
    return f'''<p>Error: login failed. Please<a href="{login_url}"> try again</a>. </p>''' 

@app.route('/logout')
def logout():
    if 'loginuser' in session:
        session.pop('loginuser')
    return f'''logged out.<br>return <a href = "{ url_for('main',name='index')}">home</a>.'''
 
if __name__=='__main__':
    app.run(debug=True)