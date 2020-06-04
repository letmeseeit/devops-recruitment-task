# First stage - build
FROM node:current-alpine AS build
WORKDIR /app
COPY package*.json /app/
RUN npm install
COPY . /app
RUN npx tsc

# Second stage - deploy
FROM node:current-alpine
WORKDIR /app
COPY --from=build /app/build ./build
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/config.json ./config.json
ENTRYPOINT [ "node" ]
CMD [ "build/index.js", "config.json" ]