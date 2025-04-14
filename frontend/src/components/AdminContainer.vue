<template>
    <div class="p-4 border rounded-lg shadow-lg max-w-lg mx-auto">
      <h2 class="text-xl font-bold mb-2">{{ title }}</h2>
      <table class="w-full border-collapse border border-gray-300">
        <thead>
          <tr class="bg-gray-200">
            <th class="border p-2" v-for="(col, index) in columns" :key="index">{{ col }}</th>
            <th class="border p-2">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(row, index) in tableData" :key="index">
            <td v-for="(col, colIndex) in columns" :key="colIndex" class="border p-2">
              <input v-model="row[col]" type="text" class="w-full p-1 border rounded">
            </td>
            <td class="border p-2 text-center">
              <button @click="removeRow(index)" class="px-2 py-1 bg-red-500 text-white rounded">X</button>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="mt-2 flex justify-between">
        <button @click="addRow" class="px-4 py-2 bg-blue-500 text-white rounded">Add Row</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      title: { type: String, default: "Dynamic Table" },
      columns: { type: Array, required: true }, // Column names
      tableData: { type: Array, required: true } // Data
    },
    methods: {
      addRow() {
        const newRow = this.columns.reduce((obj, col) => ({ ...obj, [col]: "" }), {});
        this.$emit("update-table", [...this.tableData, newRow]);
      },
      removeRow(index) {
        const newData = [...this.tableData];
        newData.splice(index, 1);
        this.$emit("update-table", newData);
      }
    }
  };
  </script>
  