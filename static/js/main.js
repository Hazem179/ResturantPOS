



const options = document.getElementsByName('opt')
const customerDisabled = Array.from(document.querySelectorAll(".customer-disabled"))
if (options) {
  Array.from(options).map(opt => {
    opt.addEventListener('change', () => {
      if (opt.value === "del") {
        customerDisabled.map(customer => {
          customer.disabled = false

        })
      } else {
        customerDisabled.map(customer => {
          customer.disabled = true

        })

      }
    })
  })
}
const categories = Array.from(document.querySelectorAll(".categories > *"))
const posTable = document.querySelector(".posTable")

if (categories) {
  categories.map(category => {
    category.addEventListener('click', () => {
      const rows = posTable.querySelectorAll("tr")
      const isExisted = Array.from(rows).some(row => row.dataset.id == category.querySelector("div").dataset.code)
      if (isExisted) {
        const row = posTable.querySelector(`tr[data-id="${category.querySelector("div").dataset.code}"]`)

        row.querySelector("#quantity").value = parseInt(row.querySelector("#quantity").value) + 1;
        row.querySelector("#price").value = parseFloat(category.querySelector("p").textContent) * parseInt(row.querySelector("#quantity").value)
      }
      else {
        let code = category.querySelector("div").dataset.code;
        let name = category.querySelector("h4").textContent;
        let price = category.querySelector("p").textContent;
        renderRow(code, name, price)
      }
      calcTotal()
    })
  })
}
function renderRow(code, name, price) {
  posTable.querySelector("tbody").insertAdjacentHTML("beforeend", `
  <tr  data-id="${code}" data-onePrice = "${price}">
  <td scope="col">
                <input type="text" class="form-control" id="code" placeholder="" readonly value="${code}" />
              </td>
              <td scope="col">
                <input type="text" class="form-control" id="type" placeholder="" readonly value="${name}" />
              </td>
              <td scope="col">
                <input type="number" class="form-control" id="price" placeholder="" readonly value="${parseFloat(price)}" />
              </td>
              <td scope="col">
                <input type="number" min="1" class="form-control" id="quantity" placeholder="" value="1" />
              </td>

              <td scope="col">

                <button class="btn btn-danger delete-row"><span style="pointer-events: none" class="bi bi-trash"></span></button>
              </td>
              </tr>
  `)
}
posTable.addEventListener("click", (e) => {

  if (e.target.classList.contains("delete-row")) {
    e.target.closest("tr").remove()
    calcTotal()
  }


})
posTable.addEventListener('input', (e) => {
  if (e.target.id === "quantity") {
    const row = e.target.closest("tr")
    row.addEventListener("change", () => {
      row.querySelector("#price").value = parseFloat(row.dataset.oneprice) * parseFloat(row.querySelector("#quantity").value)

      calcTotal()
    })
  }
})
const totalInput = document.querySelector("#total")
const discountInput = document.querySelector("#discount")
function calcTotal() {
  const rowsPrice = posTable.querySelectorAll("tr #price")

  const total = Array.from(rowsPrice).reduce((total, price) => total + parseFloat(price.value), 0)

  totalInput.value = total - (total * (discountInput.value))
}
discountInput.addEventListener("change", calcTotal)