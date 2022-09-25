from flask import Flask, url_for, request, render_template
app = Flask(__name__)
users = []


@app.route('/test_front', methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form.get('name')
      # process information
      if user in users:
         pass
      else:
         users.append(user)
      return render_template('test_front_form_output.html', names=users)
   elif request.method == 'GET':
      return render_template('test_front_form_input.html', names=users)

@app.route('/', methods = ['GET'])
def home():
   if request.method == 'POST':
        user = request.form.get('nm')
        return user 
   else:
      return render_template('Home')

# @app.route('/users/<user>', methods = ['GET'])
# def get_users(user: str):
#    global users
#    if user in users:
#       return f"User {user} Exists."
#    else:
#       users.append(user)
#       return f"The user {user} has been added."

@app.route('/users', methods = ['GET', 'POST'])
def get_users():
   global users
   if request.method == 'POST':
      user = request.form.get('name')
      if user in users:
         return f"User {user} Exists."
      else:
         users.append(user)
         return f"The user {user} has been added."

if __name__ == '__main__':
   app.run(host="0.0.0.0", port = 8080, debug = True)