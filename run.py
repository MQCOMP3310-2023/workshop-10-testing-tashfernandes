from project import create_app

## Adding some comments
# More stuff

if __name__ == '__main__':
  app = create_app()
  app.run(host = '0.0.0.0', port = 8001, debug=True) 

