json.extract! customer, :id, :name, :age, :photo, :created_at, :updated_at
json.url customer_url(customer, format: :json)
