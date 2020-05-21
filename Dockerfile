#1st Stage: Get Node and Install 
FROM node:latest as node
#Get working directory
WORKDIR /app
#Copy all items in directory
COPY . .
#Install all packages from package.json
RUN npm install
#Build app with prod 
RUN npm run build --prod

#2nd Stage: Run Node 
#FROM nginx:alpine
#FROM bitnami/nginx:latest

FROM nginxinc/nginx-unprivileged

COPY --from=node /app/dist/try-angular-flask /usr/share/nginx/html
