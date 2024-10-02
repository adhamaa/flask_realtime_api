bind = "0.0.0.0:5000"          # The address and port to bind the server to
workers = 4                     # Number of worker processes
worker_class = "eventlet"       # Use eventlet for handling requests
timeout = 120                   # Timeout for workers
loglevel = "info"               # Log level (info, debug, warning, etc.)
accesslog = "-"                 # Access log file (set to "-" for stdout)
errorlog = "-"                  # Error log file (set to "-" for stdout)
