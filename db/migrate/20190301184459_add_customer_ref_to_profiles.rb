class AddCustomerRefToProfiles < ActiveRecord::Migration[5.2]
  def change
    add_reference :profiles, :customer, foreign_key: true
  end
end
