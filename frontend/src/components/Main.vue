<template>
  <div>
    <h1>To Do List</h1>
    <form>
      <input type="text" v-model="input" />
      <button @click.prevent="submitToDo">Submit</button>
    </form>
    <ul>
        <li v-for="todo in todos" v-bind:key="todo.id">
            <Todo :todo="todo"/>
        </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
import Todo from './Todo.vue'
export default {
  data () {
    return {
      input: '',
      todos: null
    }
  },
  components: {
    Todo
  },
  methods: {
    submitToDo () {
      const todoData = {text: this.input, completed: false}
      axios.post('http://127.0.0.1:8000/todo/todo-create/', todoData)
        .then(response => response.data.id)
      this.input = ''
    }
  },
  mounted () {
    axios
      .get('http://127.0.0.1:8000/todo/todo-list')
      .then(response => (this.todos = response.data))
  },
  updated () {
    axios
      .get('http://127.0.0.1:8000/todo/todo-list')
      .then(response => (this.todos = response.data))
  }
}
</script>

<style scoped>
ul {
    list-style: none;
}
</style>
