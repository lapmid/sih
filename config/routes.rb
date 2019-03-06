Rails.application.routes.draw do
  resources :customers
  devise_for :users, :controllers => { :omniauth_callbacks => "users/omniauth_callbacks" }  
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  root to: 'customers#index'
  get '/policy', to: 'home#policy', as: 'policy'
  get 'user_details/show' => 'user_details#show', :as => 'show_user_details'
  get '/twitter_customers' => 'customers#get_twitter_users', :as => 'twitter_clients'

  resources :authentications, only: [:destroy]
  resources :user_details, only: [:index,:show]
end
