from flask import Flask

aap = Flask(__name__)

@aap.route('/<int:numero>', methods=['GET','POST'])
def hello(numero):
    return 'Hello World!'+str(numero)

if __name__ == '__main__':
    aap.run(debug=True)