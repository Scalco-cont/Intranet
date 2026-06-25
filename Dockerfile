# Stage 1: Build React
FROM node:20-alpine AS builder

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN chmod -R 755 node_modules/.bin
RUN npm run build

# Stage 2: Nginx
FROM nginx:alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 1247

CMD ["nginx", "-g", "daemon off;"]