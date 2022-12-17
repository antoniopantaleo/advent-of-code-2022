import Foundation

guard let data = Bundle.load(demo: true) else { fatalError("No Data") }

let rucksacks = data.components(separatedBy: "\n\n").compactMap { String(describing: $0) }

func partOne() {
    var counter = 0
    rucksacks.forEach {
        counter = max(counter, $0.components(separatedBy: "\n").compactMap(Int.init).reduce(0,+))
    }
    print(counter)
}

func partTwo() {
    var bestThree: [Int] = []
    for rucksack in rucksacks {
        let sum = rucksack.components(separatedBy: "\n").compactMap(Int.init).reduce(0,+)
        bestThree.append(sum)
        if bestThree.count > 3 {
            guard let min = bestThree.min(), let index = bestThree.firstIndex(of: min) else { continue }
            bestThree.remove(at: index)
        }
    }
    let sum = bestThree.reduce(0, +)
    print(sum)
}

partOne()
partTwo()
