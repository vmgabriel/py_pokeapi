# PokeAPI - Gabriel Vargas Monroy

# Technologies
- python
- fastapi
- python-dotenv
- uvicorn
- requests

# Deploy:
```bash
make run
```


# Test
a way to check the tests
```bash
make test
```


# Endpoints
GET http://127.0.0.1:8000/allBerryStats
Accept: application/json

## response

```python
{
    "berries_names": list[int],
    "min_growth_time": float,
    "median_growth_time": float,
    "max_growth_time": float,
    "variance_growth_time": float,
    "mean_growth_time": float,
    "frequency_growth_time": float
}
```