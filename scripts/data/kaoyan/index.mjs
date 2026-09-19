// 考研英语历年（2015-2024）真题核心数据集总索引

import { ky2024Exams } from "./ky_data_2024.mjs";
import { kyHistoricalArchive } from "./ky_data_2023.mjs";
import { ky2022Exams } from "./ky_data_2022.mjs";
import { ky2021Exams } from "./ky_data_2021.mjs";
import { ky2020Exams } from "./ky_data_2020.mjs";
import { ky2019Exams } from "./ky_data_2019.mjs";
import { ky2018Exams } from "./ky_data_2018.mjs";
import { ky2017Exams } from "./ky_data_2017.mjs";
import { ky2015_2017Exams } from "./ky_data_2015_2017.mjs";

export const allKaoyanExams = [
  ...ky2024Exams,        // 2024 英语一/英语二 全量 40 题 (80题)
  ...kyHistoricalArchive, // 2023 英语一/英语二 全量 40 题 (80题)
  ...ky2022Exams,        // 2022 英语一/英语二 全量 40 题 (80题)
  ...ky2021Exams,        // 2021 英语一/英语二 全量 40 题 (80题)
  ...ky2020Exams,        // 2020 英语一/英语二 全量 40 题 (80题)
  ...ky2019Exams,        // 2019 英语一/英语二 全量 40 题 (80题)
  ...ky2018Exams,        // 2018 英语一/英语二 全量 40 题 (80题)
  ...ky2017Exams,        // 2017 英语一/英语二 全量 40 题 (80题)
  ...ky2015_2017Exams    // 2015-2016 英语一 (过渡)
];
