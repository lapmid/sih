class AddFacebookTokenToUser < ActiveRecord::Migration[5.2]
  def change
    change_table :users do |t|
      t.string   :facebook_token
      t.string   :name
    end
  end
end
