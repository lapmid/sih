class Customer < ApplicationRecord
    mount_uploader :photo, PhotoUploader
end
