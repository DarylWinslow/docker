from flask import Flask
from flask import request
from os import listdir
from os.path import isfile, join

def multiples_of_3_or_5():
        for number in xrange(1000):
            if not number % 3 or not number % 5:
                yield number

    print sum(multiples_of_3_or_5())


def fib():
        x,y = 0,1
        while True:
            yield x
            x,y = y, x+y

    def even(seq):
        for number in seq:
            if not number % 2:
                yield number

    def under_a_million(seq):
        for number in seq:
            if number > 1000000:
                break
            yield number

    print sum(even(under_a_million(fib())))


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/'+f.filename)
    return '',201
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)



app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()



@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


#function to return names of files in upload directory
def list_files():
        mypath = "/home/user/lab4/docker/python-flask/my_application/upload"
	onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
	return (onlyfiles)
