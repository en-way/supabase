// 考研英语历年（2015-2024）真题核心数据集总索引

import { ky2024Exams } from "./ky_data_2024.mjs";
import { kyHistoricalArchive } from "./ky_data_2023.mjs";
import { ky2021_2022Exams } from "./ky_data_2021_2022.mjs";
import { ky2018_2020Exams } from "./ky_data_2018_2020.mjs";
import { ky2015_2017Exams } from "./ky_data_2015_2017.mjs";

export const allKaoyanExams = [
  ...ky2024Exams,
  ...kyHistoricalArchive,
  ...ky2021_2022Exams,
  ...ky2018_2020Exams,
  ...ky2015_2017Exams
];
