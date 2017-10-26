# coding: utf-8
char_dir = {
    "&Alpha;": "Α",
    "&Delta;": "Δ",
    "&Eta;": "Η",
    "&Kappa;": "Κ",
    "&Nu;": "Ν",
    "&Pi;": "Π",
    "&Tau;": "Τ",
    "&Chi;": "Χ",
    "&alpha;": "α",
    "&delta;": "δ",
    "&eta;": "η",
    "&kappa;": "κ",
    "&nu;": "ν",
    "&pi;": "π",
    "&sigma;": "σ",
    "&phi;": "φ",
    "&omega;": "ω",
    "&piv;": "ϖ",
    "&prime;": "′",
    "&frasl;": "⁄",
    "&real;": "ℜ",
    "&larr;": "←",
    "&darr;": "↓",
    "&lArr;": "⇐",
    "&dArr;": "⇓",
    "&part;": "∂",
    "&nabla;": "∇",
    "&ni;": "∋",
    "&minus;": "−",
    "&prop;": "∝",
    "&and;": "∧",
    "&cup;": "∪",
    "&sim;": "∼",
    "&ne;": "≠",
    "&ge;": "≥",
    "&nsub;": "⊄",
    "&oplus;": "⊕",
    "&sdot;": "⋅",
    "&lfloor;": "⌊",
    "&spades;": "♠",
    "&diams;": "♦",
    "&cent;": "¢",
    "&yen;": "¥",
    "&uml;": "¨",
    "&laquo;": "«",
    "&reg;": "®",
    "&plusmn;": "±",
    "&acute;": "´",
    "&lt;": "<",
    "&#913;": "Α",
    "&#916;": "Δ",
    "&#919;": "Η",
    "&#922;": "Κ",
    "&#925;": "Ν",
    "&#928;": "Π",
    "&#932;": "Τ",
    "&#935;": "Χ",
    "&#945;": "α",
    "&#948;": "δ",
    "&#951;": "η",
    "&#954;": "κ",
    "&#957;": "ν",
    "&#960;": "π",
    "&#963;": "σ",
    "&#966;": "φ",
    "&#969;": "ω",
    "&#982;": "ϖ",
    "&#8242;": "′",
    "&#8260;": "⁄",
    "&#8476;": "ℜ",
    "&#8592;": "←",
    "&#8595;": "↓",
    "&#8656;": "⇐",
    "&#8659;": "⇓",
    "&#8706;": "∂",
    "&#8711;": "∇",
    "&#8715;": "∋",
    "&#8722;": "−",
    "&#8733;": "∝",
    "&#8869;": "∧",
    "&#8746;": "∪",
    "&#8764;": "∼",
    "&#8800;": "≠",
    "&#8805;": "≥",
    "&#8836;": "⊄",
    "&#8853;": "⊕",
    "&#8901;": "⋅",
    "&#8970;": "⌊",
    "&#9824;": "♠",
    "&#9830;": "♦",
    "&#162;": "¢",
    "&#165;": "¥",
    "&#168;": "¨",
    "&#171;": "«",
    "&#174;": "®",
    "&#177;": "±",
    "&#180;": "´",
    "&#60;": "<",
    "&Beta;": "Β",
    "&Epsilon;": "Ε",
    "&Theta;": "Θ",
    "&Lambda;": "Λ",
    "&Xi;": "Ξ",
    "&Rho;": "Ρ",
    "&Upsilon;": "Υ",
    "&Psi;": "Ψ",
    "&beta;": "β",
    "&epsilon;": "ε",
    "&theta;": "θ",
    "&lambda;": "λ",
    "&xi;": "ξ",
    "&rho;": "ρ",
    "&tau;": "τ",
    "&chi;": "χ",
    "&thetasym;": "ϑ",
    "&bull;": "•",
    "&Prime;": "″",
    "&weierp;": "℘",
    "&trade;": "™",
    "&uarr;": "↑",
    "&harr;": "↔",
    "&uArr;": "⇑",
    "&hArr;": "⇔",
    "&exist;": "∃",
    "&isin;": "∈",
    "&prod;": "∏",
    "&lowast;": "∗",
    "&infin;": "∞",
    "&or;": "∨",
    "&int;": "∫",
    "&cong;": "≅",
    "&equiv;": "≡",
    "&sub;": "⊂",
    "&sube;": "⊆",
    "&otimes;": "⊗",
    "&lceil;": "⌈",
    "&rfloor;": "⌋",
    "&clubs;": "♣",
    "&pound;": "£",
    "&brvbar;": "¦",
    "&copy;": "©",
    "&not;": "¬",
    "&macr;": "¯",
    "&sup2;": "²",
    "&micro;": "µ",
    "&gt;": ">",
    "&#914;": "Β",
    "&#917;": "Ε",
    "&#920;": "Θ",
    "&#923;": "Λ",
    "&#926;": "Ξ",
    "&#929;": "Ρ",
    "&#933;": "Υ",
    "&#936;": "Ψ",
    "&#946;": "β",
    "&#949;": "ε",
    "&#952;": "θ",
    "&#955;": "λ",
    "&#958;": "ξ",
    "&#961;": "ρ",
    "&#964;": "τ",
    "&#967;": "χ",
    "&#977;": "ϑ",
    "&#8226;": "•",
    "&#8243;": "″",
    "&#8472;": "℘",
    "&#8482;": "™",
    "&#8593;": "↑",
    "&#8596;": "↔",
    "&#8657;": "⇑",
    "&#8660;": "⇔",
    "&#8707;": "∃",
    "&#8712;": "∈",
    "&#8719;": "∏",
    "&#8727;": "∗",
    "&#8734;": "∞",
    "&#8870;": "∨",
    "&#8747;": "∫",
    "&#8773;": "≅",
    "&#8801;": "≡",
    "&#8834;": "⊂",
    "&#8838;": "⊆",
    "&#8855;": "⊗",
    "&#8968;": "⌈",
    "&#8971;": "⌋",
    "&#9827;": "♣",
    "&#163;": "£",
    "&#166;": "¦",
    "&#169;": "©",
    "&#172;": "¬",
    "&#175;": "¯",
    "&#178;": "²",
    "&#181": "µ",
    "&#62;": ">",
    "&Gamma;": "Γ",
    "&Zeta;": "Ζ",
    "&Iota;": "Ι",
    "&Mu;": "Μ",
    "&Omicron;": "Ο",
    "&Sigma;": "Σ",
    "&Phi;": "Φ",
    "&Omega;": "Ω",
    "&gamma;": "γ",
    "&zeta;": "ζ",
    "&iota;": "ι",
    "&mu;": "μ",
    "&omicron;": "ο",
    "&sigmaf;": "ς",
    "&upsilon;": "υ",
    "&psi;": "ψ",
    "&upsih;": "ϒ",
    "&hellip;": "…",
    "&oline;": "‾",
    "&image;": "ℑ",
    "&alefsym;": "ℵ",
    "&rarr;": "→",
    "&crarr;": "↵",
    "&rArr;": "⇒",
    "&forall;": "∀",
    "&empty;": "∅",
    "&notin;": "∉",
    "&sum;": "∑",
    "&radic;": "√",
    "&ang;": "∠",
    "&cap;": "∩",
    "&there4;": "∴",
    "&asymp;": "≈",
    "&le;": "≤",
    "&sup;": "⊃",
    "&supe;": "⊇",
    "&perp;": "⊥",
    "&rceil;": "⌉",
    "&loz;": "◊",
    "&hearts;": "♥",
    "&iexcl;": "¡",
    "&curren;": "¤",
    "&sect;": "§",
    "&ordf;": "ª",
    "&deg;": "°",
    "&sup3;": "³",
    "&quot;": "\"",
    "&#915;": "Γ",
    "&#918;": "Ζ",
    "&#921;": "Ι",
    "&#924;": "Μ",
    "&#927;": "Ο",
    "&#931;": "Σ",
    "&#934;": "Φ",
    "&#937;": "Ω",
    "&#947;": "γ",
    "&#950;": "ζ",
    "&#953;": "ι",
    "&#956;": "μ",
    "&#959;": "ο",
    "&#962;": "ς",
    "&#965;": "υ",
    "&#968;": "ψ",
    "&#978;": "ϒ",
    "&#8230;": "…",
    "&#8254;": "‾",
    "&#8465;": "ℑ",
    "&#8501;": "ℵ",
    "&#8594;": "→",
    "&#8629;": "↵",
    "&#8658;": "⇒",
    "&#8704;": "∀",
    "&#8709;": "∅",
    "&#8713;": "∉",
    "&#8722;": "∑",
    "&#8730;": "√",
    "&#8736;": "∠",
    "&#8745;": "∩",
    "&#8756;": "∴",
    "&#8773;": "≈",
    "&#8804;": "≤",
    "&#8835;": "⊃",
    "&#8839;": "⊇",
    "&#8869;": "⊥",
    "&#8969;": "⌉",
    "&#9674;": "◊",
    "&#9829;": "♥",
    "&#161;": "¡",
    "&#164;": "¤",
    "&#167;": "§",
    "&#170;": "ª",
    "&#176;": "°",
    "&#179;": "³",
    "&#34;": "\"",
    "&#39;": "'",
    "&times;": "×",
    "&#215;": "×",
    "&divide;": "÷",
    "&#247;": "÷",
    "&apos;": "'",
    "&#39;": "'",
    "&nbsp;": " ",
    "&#160;": " ",
    "&ensp;": " ",
    "&emsp;": " ",
}

and_dir = {
    "&amp;": "&",
    "&#38;": "&",
}