# Use Node.js LTS image as base
FROM node:lts-alpine

# Set working directory
WORKDIR /app

# Copy the frontend folder (including package.json and package-lock.json)
COPY ./frontend .

# Install dependencies
RUN npm install


# Expose the port Next.js will run on
EXPOSE 3000

# Run the Next.js app
CMD ["npm", "start"]
