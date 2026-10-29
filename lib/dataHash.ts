/**
 * Enway 确定性数据规范化序列化与 SHA-256 哈希指纹引擎
 * 用于客户端与云端用户研习数据、考务配置比对，实现 0 网络消耗的防重与防滥用硬阻断。
 */

/**
 * 递归规范化序列化对象：确保对象的 Key 按照字母表字典序严格排序，
 * 数组元素递归处理，消除因属性书写顺序差异导致的虚假指纹不一致。
 */
export function canonicalJsonStringify(obj: any): string {
  if (obj === null || obj === undefined) {
    return "null";
  }
  if (typeof obj !== "object") {
    return JSON.stringify(obj);
  }
  if (Array.isArray(obj)) {
    return `[${obj.map((item) => canonicalJsonStringify(item)).join(",")}]`;
  }
  const sortedKeys = Object.keys(obj).sort();
  const keyValPairs = sortedKeys.map(
    (key) => `${JSON.stringify(key)}:${canonicalJsonStringify(obj[key])}`
  );
  return `{${keyValPairs.join(",")}}`;
}

/**
 * 计算传入数据的确定性 SHA-256 十六进制散列指纹
 * 优先采用浏览器原生高性能 Web Crypto API (crypto.subtle)
 */
export async function computeDataHash(data: any): Promise<string> {
  const canonicalStr = canonicalJsonStringify(data);
  if (typeof crypto !== "undefined" && crypto.subtle) {
    try {
      const encoder = new TextEncoder();
      const dataBuffer = encoder.encode(canonicalStr);
      const hashBuffer = await crypto.subtle.digest("SHA-256", dataBuffer);
      const hashArray = Array.from(new Uint8Array(hashBuffer));
      return hashArray.map((b) => b.toString(16).padStart(2, "0")).join("");
    } catch (e) {
      console.warn("[DataHash] Web Crypto digest error, falling back:", e);
    }
  }

  // 环境无 Web Crypto 时的轻量确定性散列回退 (FNV-1a 32-bit + DJB2 组合)
  let h1 = 0x811c9dc5;
  let h2 = 5381;
  for (let i = 0; i < canonicalStr.length; i++) {
    const code = canonicalStr.charCodeAt(i);
    h1 ^= code;
    h1 = Math.imul(h1, 0x01000193);
    h2 = ((h2 << 5) + h2) ^ code;
  }
  const p1 = (h1 >>> 0).toString(16).padStart(8, "0");
  const p2 = (h2 >>> 0).toString(16).padStart(8, "0");
  return `hash-${p1}${p2}`;
}
