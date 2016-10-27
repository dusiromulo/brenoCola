import sys
from view.application import BrenoColaApplication

if __name__ == "__main__":
    app = BrenoColaApplication(sys.argv)
    sys.exit(app.exec_())
