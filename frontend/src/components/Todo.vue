<template>
  <div class="row">
    <!-- <form>
        {{ this.todo }}
        <input type="text">
        <button>Edit</button>
    </form> -->
        <div class="col-6">
            <input v-if="isEdit" type="text" v-model="inputValue" id="editInput" v-on:keyup="inputUpdate" ref="editInput"/>
            <input v-else type="text" v-model="inputValue" disabled/>
        </div>
        <div class="col-auto">
            <button v-if="isEdit" @click.prevent="submitEditedToDo(todo.id)">S Edit</button>
            <button v-else @click.prevent="editToDo(todo.id)">Edit</button>
        </div>
        <div class="col-auto">
            <button @click.prevent="deleteToDo(todo.id)">Delete</button>
        </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Todo',
  props: {
    todo: this.todo
  },
  data () {
    return {
      isEdit: false,
      inputValue: this.todo.text
    }
  },
  updated () {
    this.isEdit ? this.$refs.editInput.focus() : ''
  },
  methods: {
    inputUpdate (e) {
      this.inputValue = e.target.value
    },
    submitEditedToDo (id) {
      const todoUpdatedData = {text: this.inputValue, completed: false}
      axios.post(`http://127.0.0.1:8000/todo/todo-update/${id}/`, todoUpdatedData)
        .then(response => response.data)
      this.isEdit = false
    },
    editToDo (id) {
      this.isEdit = true
    },
    deleteToDo (id) {
      axios.delete(`http://127.0.0.1:8000/todo/todo-delete/${id}/`)
        .then(response => (this.todos = response.data))
    }
  }
}
</script>

<style scoped>

</style>
