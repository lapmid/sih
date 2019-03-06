require 'twitter'
class CustomersController < ApplicationController
  before_action :set_customer, only: [:show, :edit, :update, :destroy]
  before_action :authenticate_user!
  # GET /customers
  # GET /customers.json
  def index
    @customers = Customer.all
  end

  # GET /customers/1
  # GET /customers/1.json
  def show
    cmd = 'sudo python sih/test2.py "'+@customer.name+'" '+@customer.photo.url
    # puts cmd
    # output = `#{cmd}`
    output=%x{#{cmd}}
    @missing = "#{output}"
    
  end

  

  def get_twitter_users
    @clients=get_users("manthan")
      # format.json { render json: json_format(@clients),status: :created }
    render json: {status: 'SUCCESS', message: 'Loaded all posts', data: @clients}, status: :ok
    
  end

  

  # GET /customers/new
  def new
    @customer = Customer.new
  end

  # GET /customers/1/edit
  def edit
  end

  # POST /customers
  # POST /customers.json
  def create
    @customer = Customer.new(customer_params)

    respond_to do |format|
      if @customer.save
        format.html { redirect_to customers_url, notice: 'Customer was successfully created.' }
        format.json { render :index, status: :created, location: customers_url }
        flash[:notice] = "Doubt was successfully Posted You Will Be Contacted Soon By Our Support Team."
        flash[:success] = "If need Instant help Drop A Message With Your Name On Bottom Right Corner"
      else
        format.html { render :new }
        format.json { render json: @customer.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /customers/1
  # PATCH/PUT /customers/1.json
  def update
    respond_to do |format|
      if @customer.update(customer_params)
        format.html { redirect_to customers_url, notice: 'Customer was successfully updated.' }
        format.json { render :index, status: :ok, location: customers_url }
      else
        format.html { render :edit }
        format.json { render json: @customer.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /customers/1
  # DELETE /customers/1.json
  def destroy
    @customer.destroy
    respond_to do |format|
      format.html { redirect_to customers_url, notice: 'Customer was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
  # Use callbacks to share common setup or constraints between actions.
  def set_customer
      @customer = Customer.find(params[:id])
  end
  private
  def get_users(userName)
    MyTwitter.user_search(userName)
  end
    # Never trust parameters from the scary internet, only allow the white list through.
    def customer_params
      params.require(:customer).permit(:name, :age, :photo,:remove_image)
    end
end
