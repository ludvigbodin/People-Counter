export default async function getCounterValues(){
    const response = await fetch("/count")
    const result = await response.json();
    return result;
}