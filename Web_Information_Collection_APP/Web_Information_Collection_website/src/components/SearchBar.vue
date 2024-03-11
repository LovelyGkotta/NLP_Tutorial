<template>
    <div class="search-box">
      <div class="search-container">
        <input
          type="text"
          v-model="keyword"
          placeholder="type a URL"
        />
        <button @click="sendData">Search</button>
      </div>
      <div class="arc"></div>
    </div>
  </template>
  
  <script>
  // export default{
  //   data(){
  //     return {
  //       keyword: ""
  //     }
  //   },
  //   methods: {
  //     async sendData(){
  //         try {
  //       console.log("***********point 1***********");
  //       const response = await fetch('http://localhost:5173/api/data', {
  //         method: 'POST', // 你需要指定请求的方法为 POST
  //         headers: {
  //           'Content-Type': 'application/json'
  //         },
  //         body: JSON.stringify({ data: this.keyword }) // 解除注释，发送数据
  //       });
  //       // console.log("***********point 1.1***********");
  //       // const result = await response.json();
  //       // console.log("***********point 1.2***********");
  //       // this.message = result.message;
  //       // console.log(result.message);
  //       } catch (error) {
  //         console.error('Error:', error);
  //       }
  //     }
  //   }
  // }
  
export default {
  data() {
    return {
      keyword: '',
      message: 'testing-meg' // 你可能忘记定义 message，我添加了这一行
    };
  },
  methods: {
    async sendData() {
      console.log("***********point 0***********");
      try {
        console.log("***********point 1***********");
        const response = await fetch('http://localhost:5173/api/data', {
          method: 'POST', // 你需要指定请求的方法为 POST
          // headers: {
          //   'Content-Type': 'application/json'
          // },
          body: JSON.stringify({ data: this.keyword }) // 解除注释，发送数据
        });
        console.log("***********point 1.1***********");
        const result = await response.json();
        console.log("***********point 1.2***********");
        this.message = result.message;
        console.log(result.message);
      } catch (error) {
        console.error('Error:', error);
      }
    }
  }
};
</script>
  
  <style scoped>
  .search-box {
    position: relative;
    width: 300px;
    margin: 20px auto;
  }
  
  .search-container {
    display: flex;
    align-items: center;
  }
  
  input {
    flex: 1;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 20px;
    outline: none;
  }
  
  button {
    padding: 10px;
    border: none;
    border-radius: 20px;
    background-color: #007bff;
    color: #fff;
    cursor: pointer;
  }
  </style>
  