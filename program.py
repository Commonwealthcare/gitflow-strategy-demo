# This script is only simulating a deployment script running in automated deployments.

print("This is a simulation of deployment script written by Harivardhan.\n")
print("It accesses secrets and variables defined for the environment in Repo Settings as follows:\n\n")

print("DB_URL: ${{ vars.DB_URL }}\n")
print("DB_USERNAME: ${{ vars.DB_USERNAME }}\n")
print("DB_PASSWORD: ${{ vars.DB_PASSWORD }}\n")

print("Deployment completed.\n")

print("------------------------------------------------------------------------------------------------------------------")
print("Initial Commit - 10/30")

print("Fixing variables and adding parenthesis - 10/31")