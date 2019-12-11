function confirmarEliminacion(id) {
  Swal.fire({
    title: 'Estas seguro?',
    text: "No podras deshacer la accion",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, eliminar!'
  }).then((result) => {
    if (result.value) {
       
    }
  })

}