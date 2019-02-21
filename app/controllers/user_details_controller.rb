class UserDetailsController < ApplicationController

    def index
        @users = User.all
    end
end
