<template>
  <div class="d-flex align-items-center" style="height:300px;" id="searchForm">
    <div class="col-12 d-flex justify-content-center">
        <input class="col-10" type="text" id="searchInput" placeholder="영화, 배우, 제작진을 검색하세요." aria-label="영화, 배우, 제작진을 검색하세요.">
        <button class="btn btn-outline-secondary fw-bold" type="button" id="searchButton">Search</button>
    </div>
  </div>
</template>
<script>
export default {


}
</script>

<style>
#searchButton {
    background: linear-gradient(to right, rgba(30,213,169, 1) 30%, 
                rgba(1,180,228, 1) 100%);
    border-radius: 20px;
    border: none;
    color: white;
    
}
#searchInput {
    border-radius: 20px;
}
#searchForm {
    background-color: rgba(216, 214, 226, 0.301);
}
</style>