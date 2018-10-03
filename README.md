# es storage sizer
This is a flask api which takes input various parameters and return capacity response

# Endpoints

1. `/es/`: This endpoint takes multiple inputs as query parameters and returns storage capacity of ES nodes needed to store data.
   Below is the sample request and response for this endpoint, you can change the values (e.g. "retention_day" based on your customer requirment)

   
    ➜ curl "http://0.0.0.0:5000/es/?bytes_per_lines=2560&lines_per_sec=10&pods_per_nodes=100&number_of_nodes=7&retention_days=30"
    
# run api locally

  
    ➜ python capacity_planner.py

# requirments
python 2.7
Flask==1.0.2 (pip install Flask==1.0.2 )