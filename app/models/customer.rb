class Customer < ApplicationRecord
    has_many :profiles,dependent: :destroy
    mount_uploader :photo, PhotoUploader
end
