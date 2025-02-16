FROM node:lts-alpine AS builder
WORKDIR /app
COPY ./package.json /app/
RUN npm i
COPY . ./
RUN npm run build

FROM node:lts-alpine AS runner
WORKDIR /app
COPY --from=builder /app/.output ./
ENV HOST=0.0.0.0 NODE_ENV=production
ENV NODE_ENV=production
EXPOSE 3000
CMD ["node", "/app/server/index.mjs"]