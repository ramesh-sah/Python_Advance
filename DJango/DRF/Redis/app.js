import axios from 'axios';
import Redis from 'ioredis';
const apiURL = "https://fakestoreapi.com/products/"
// const getProducts = async () => {
//     try {
//         let response = await axios.get(apiURL)
//         return {
//             ...response.data, 'source': 'APi'
//         }
//     } catch {
//         console.log("unable to make api request")
//     }
// }
// const beforeApiCallTime = new Date().getTime()
// let allproducts = await getProducts()
// const afterApiCallTime = new Date().getTime()
// allproducts.responseTime = afterApiCallTime - beforeApiCallTime + 'ms'
// console.log("all products :", allproducts)


//with redis 
const redisOption = {
    host: '127.0.0.1', //redis host
    port: 6379

};
const redisClient = new Redis(redisOption);

const getProducts = async () => {
    //check  if data is available in cache
    let cachedProductData = await redisClient.get('products')
    if (cachedProductData) {
        return { ...JSON.parse(cachedProductData), 'source': 'cached Redis' }
    } else {
        try {
            let response = axios.get(apiURL);
            redisClient.set('products', JSON.stringify(response.data), 'EX', 60);
            return { ...response.data, 'Source': "API" }
        }
        catch {
            console.log("error fetching data")

        }
    }

}
const beforeApiCallTime = new Date().getTime()
let allproducts = await getProducts()
const afterApiCallTime = new Date().getTime()
allproducts.responseTime = afterApiCallTime - beforeApiCallTime + 'ms'
console.log("all products :", allproducts)