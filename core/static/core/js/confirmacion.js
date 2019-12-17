function confirmarEliminacion(id){
    Swal.fire({
        title: 'Estas seguro?',
        text: "No podras deshacer esta accion",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'si, Eliminar!',
        cancelbuttonText: 'Cancelar'
      }).then((result) => {
        if (result.value) {
            window.location.href = "/eliminar-cliente/"+id+"/";
        }
      })
}


function confirmarEliminacion2(id){
  Swal.fire({
      title: 'Estas seguro?',
      text: "No podras deshacer esta accion",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'si, Eliminar!',
      cancelbuttonText: 'Cancelar'
    }).then((result) => {
      if (result.value) {
          window.location.href = "/eliminar-ot/"+id+"/";
      }
    })
}
function confirmarEliminacion3(id){
  Swal.fire({
      title: 'Estas seguro?',
      text: "No podras deshacer esta accion",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'si, Eliminar!',
      cancelbuttonText: 'Cancelar'
    }).then((result) => {
      if (result.value) {
          window.location.href = "/eliminar-tecnico/"+id+"/";
      }
    })
}