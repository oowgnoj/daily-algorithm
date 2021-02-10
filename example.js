const sampleCsv = 'ACCOUNT_NUMBER,ACCOUNT_ID,DATE,SCORE,SCORE_1\n954332033,141310885,09/13/2020,92,84\n954332033,141310885,09/14/2020,74,83\n954332033,141310885,09/15/2020,94,94';
const elements = sampleCsv.split('\n')[0].split(',')
const answers = sampleCsv.split('\n').slice(1)
let result = []
for (let answer of answers){
    const arr = answer.split(',')
    let temp ={}
    for (let i = 0 ; i < elements.length; i++){
        temp[elements[i]] = arr[i]
    }

    result.push(temp)
}

console.log(result)