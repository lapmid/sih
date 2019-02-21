class UserDetailsController < ApplicationController

    def index
        @users = User.all
        @likes = get_object(current_user.facebook_token, 'me?fields=likes')
    end

    def fbgraph(token)
        Koala::Facebook::API.new(token)
    end
      
    def get_object(token, id, args = {}, options = {}, &block)
        fbgraph(token).get_object(id, args, options, &block)
    end
end
